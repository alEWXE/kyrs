import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import psutil
import time

# Определение функции для получения статистики системы
def get_system_stats(duration=20):
    cpu_usage = []
    memory_usage = []
    network_traffic = []
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_usage.append(psutil.cpu_percent())
        memory_usage.append(psutil.virtual_memory().percent)
        network_traffic.append(psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv)
        time.sleep(1)
    return cpu_usage, memory_usage, network_traffic

# Создание Streamlit приложения
def main():
    st.title("Мониторинг ресурсов системы")

    # Получение статистики системы
    cpu_usage, memory_usage, network_traffic = get_system_stats()

    # Построение графика загрузки CPU
    st.subheader("Загрузка CPU (%)")
    fig_cpu, ax_cpu = plt.subplots()
    ax_cpu.plot(cpu_usage, color='tab:blue')
    ax_cpu.set_xlabel('Время (с)')
    ax_cpu.set_ylabel('Загрузка CPU (%)', color='tab:blue')
    ax_cpu.tick_params('y', colors='tab:blue')
    ax_cpu.xaxis.set_major_locator(MaxNLocator(integer=True))
    st.pyplot(fig_cpu)

    # Построение графика использования памяти
    st.subheader("Использование памяти (%)")
    fig_mem, ax_mem = plt.subplots()
    ax_mem.plot(memory_usage, color='tab:red')
    ax_mem.set_xlabel('Время (с)')
    ax_mem.set_ylabel('Использование памяти (%)', color='tab:red')
    ax_mem.tick_params('y', colors='tab:red')
    ax_mem.xaxis.set_major_locator(MaxNLocator(integer=True))
    st.pyplot(fig_mem)

    # Построение графика сетевого трафика
    st.subheader("Сетевой трафик (байт)")
    fig_net, ax_net = plt.subplots()
    ax_net.plot(network_traffic, color='tab:green')
    ax_net.set_xlabel('Время (с)')
    ax_net.set_ylabel('Сетевой трафик (байт)', color='tab:green')
    ax_net.tick_params('y', colors='tab:green')
    ax_net.xaxis.set_major_locator(MaxNLocator(integer=True))
    st.pyplot(fig_net)

if __name__ == "__main__":
    main()
