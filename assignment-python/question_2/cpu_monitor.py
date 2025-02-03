import psutil
import time

CPU_THRESHOLD = 80

def monitor_cpu_usage():
    print("Monitoring CPU usage... Press Ctrl+C to stop.")

    try:
        # Initial call to avoid incorrect first 0% reading
        psutil.cpu_percent(interval=1) 

        while True:
            # Get the overall CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)  

            # Display an alert if CPU usage exceeds the threshold
            if cpu_usage > CPU_THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage:.2f}%")

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")

if __name__ == "__main__":
    monitor_cpu_usage()