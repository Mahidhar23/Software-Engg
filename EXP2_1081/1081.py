from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Path to the Edge WebDriver
edge_driver_path = r"C:/Users/hp/Downloads/edgedriver_win64/msedgedriver.exe"

# Path to the HTML file
html_file_path = r"C:/software-Engg/model.html"

# Verify the file exists
if not os.path.exists(html_file_path):
    print(f"Error: HTML file not found at {html_file_path}. Please check the path.")
    exit(1)

# Set up the WebDriver
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

try:
    # Open the HTML file
    driver.get(f"file://{html_file_path}")

    # --- Stage 1: Hard-coding variables ---
    a, b, c = 51, 91, 12  # Example hard-coded values
    driver.find_element(By.ID, 'a').send_keys(str(a))
    driver.find_element(By.ID, 'b').send_keys(str(b))
    driver.find_element(By.ID, 'c').send_keys(str(c))
    driver.find_element(By.ID, 'calculate').click()
    time.sleep(2)  # Wait for result
    print("Result after hard-coding:", driver.find_element(By.ID, 'result').text)

    # Clear the form for the next stage
    for field in ['a', 'b', 'c']:
        driver.execute_script("arguments[0].value = '';", driver.find_element(By.ID, field))

    # --- Stage 2: Keyboard input ---
    a, b, c = map(int, input("Enter coefficients a, b, c (space-separated): ").split())
    driver.find_element(By.ID, 'a').send_keys(str(a))
    driver.find_element(By.ID, 'b').send_keys(str(b))
    driver.find_element(By.ID, 'c').send_keys(str(c))
    driver.find_element(By.ID, 'calculate').click()
    time.sleep(2)
    print("Result after keyboard input:", driver.find_element(By.ID, 'result').text)

    # Clear the form for the next stage
    for field in ['a', 'b', 'c']:
        driver.execute_script("arguments[0].value = '';", driver.find_element(By.ID, field))

    # --- Stage 3: Reading from a file (single input) ---
    with open(r"C:/Users/hp/Documents/input_single.txt", "r") as file:
        a, b, c = map(int, file.readline().strip().split())
    driver.find_element(By.ID, 'a').send_keys(str(a))
    driver.find_element(By.ID, 'b').send_keys(str(b))
    driver.find_element(By.ID, 'c').send_keys(str(c))
    driver.find_element(By.ID, 'calculate').click()
    time.sleep(2)
    print("Result after reading from file:", driver.find_element(By.ID, 'result').text)

    # Clear the form for the next stage
    for field in ['a', 'b', 'c']:
        driver.execute_script("arguments[0].value = '';", driver.find_element(By.ID, field))

    # --- Stage 4: Reading from a file (multiple sets of input) ---
    with open(r"C:/Users/hp/Documents/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line or len(line.split()) != 3:  # Skip empty or malformed lines
                continue
            a, b, c = map(int, line.split())
            driver.find_element(By.ID, 'a').send_keys(str(a))
            driver.find_element(By.ID, 'b').send_keys(str(b))
            driver.find_element(By.ID, 'c').send_keys(str(c))
            driver.find_element(By.ID, 'calculate').click()
            time.sleep(2)
            print(f"Input ({a}, {b}, {c}):", driver.find_element(By.ID, 'result').text)
            for field in ['a', 'b', 'c']:
                driver.execute_script("arguments[0].value = '';", driver.find_element(By.ID, field))

finally:
    driver.quit()
