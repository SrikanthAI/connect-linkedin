from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--executable_path=C:\\Users\\konne\\Desktop\\Connect Linkedin Project\\chromedriver')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.linkedin.com/login?")

email = driver.find_element(By.ID, 'username')
email.send_keys('charan@pascalcase.com')
sleep(2)

password = driver.find_element(By.ID, 'password')
password.send_keys('Durga8499856056')
sleep(2)

wait = WebDriverWait(driver, 10)
log_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']")))
log_in_button.click()
sleep(2)

# Replace with the actual LinkedIn profile URLs
links = ["https://www.linkedin.com/in/ayush-kishor-8a81b01b3/"]

# After collecting links
for link in links:
    try:
        driver.get(link)
        sleep(5)  # Wait for the page to load

        # Wait for the profile name element to be visible
        profile_name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h1[@class="text-heading-xlarge inline t-24 v-align-middle break-words"]')))
        driver.execute_script("arguments[0].scrollIntoView();", profile_name_element)
        profile_name = profile_name_element.text
        print(profile_name)
        sleep(5)
        try:
            # Locate the "Connect" button using the provided HTML code
                connect_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Invite {0} to connect'])[2]".format(profile_name))))

                # Click the "Connect" button to open the connection request dialog
                connect_button.click()
                print("clicked on connect button")
                # Wait for the dialog to appear
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Add a note']")))

                # Find and click the "Add a note" button to open the message input field
                add_note_button = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
                add_note_button.click()
                print("clicked on add note button")
                # Find the message input field and enter your desired message
                message_input = driver.find_element(By.XPATH, "//textarea[@name='message']")
                message = "Hello, I'd like to connect with you on LinkedIn."
                message_input.send_keys(message)
                print("message is added to textarea")

                # Find and click the "Send now" button to send the connection request with the message
                send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
                send_button.click()

                print("Connection request sent successfully!")
        except:
            try:
                #Locate the "more" button
                more_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//button[@aria-label='More actions'])[2]")))
                more_button.click()
                
                # Locate the "Connect" button using the provided HTML code
                connect_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@aria-label='Invite {0} to connect'])[2]".format(profile_name))))
                # Click the "Connect" button to open the connection request dialog
                connect_button.click()
                print("clicked on connect button")
                # Wait for the dialog to appear
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Add a note']")))

                # Find and click the "Add a note" button to open the message input field
                add_note_button = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
                add_note_button.click()
                print("clicked on add note button")
                # Find the message input field and enter your desired message
                message_input = driver.find_element(By.XPATH, "//textarea[@name='message']")
                message = "Hello, I'd like to connect with you on LinkedIn."
                message_input.send_keys(message)
                print("message is added to textarea")

                # Find and click the "Send now" button to send the connection request with the message
                send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
                send_button.click()

                print("Connection request sent successfully!")

            except Exception as e:
                print("Exception:", e)
                
    except Exception as e:
        print("Exception:", e)

# Close the browser
driver.quit()

