# CPU Usage Monitoring Script

## Question 2

#### Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:

- The program should continuously monitor the CPU usage of the local machine.
- If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
- The program should run indefinitely until interrupted.
- The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

## Hint

- The `psutil` library in Python can be used to retrieve system information, including CPU usage. You can install it using `pip install psutil`
- Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

### Expected Output:
- Monitoring CPU usage...
- Alert! CPU usage exceeds threshold: 85%
- Alert! CPU usage exceeds threshold: 90%
- ... (continues until interrupted) 

---
This Python script monitors CPU usage and alerts the user when usage exceeds a defined threshold.

## Prerequisites

Ensure you have `psutil` installed before running the script. If not, install it using:

```bash
pip install -r requirements.txt
```



## Script: `cpu_monitor.py`

## Usage

1. Open a terminal and navigate to the script's directory.
3. Run the script using:

   ```bash
   python cpu_monitor.py
   ```

4. The script will continuously monitor CPU usage. If the CPU usage exceeds 80%, an alert will be displayed.
5. To stop the script, press `Ctrl + C`.

## Customization

- You can change the CPU threshold by modifying the `CPU_THRESHOLD` variable.
- Adjust the `interval` in `psutil.cpu_percent(interval=1)` to change the monitoring frequency.

## Notes

- Running the script requires appropriate permissions.
- Ensure `psutil` is installed before execution.