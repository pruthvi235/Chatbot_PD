from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the Selenium WebDriver
driver = webdriver.Chrome(executable_path="Downloads\chromedriver_win32\chromedriver.exe")  # Change this to your chromedriver path

# Open the chatbot webpage
driver.get("https://khaanvaani.streamlit.app/")  # Replace with the URL of the chatbot

# Find the chat input element
chat_input = driver.find_element_by_id("InputInstructions")  # Replace "chat-input" with the actual chat input field ID

# Start a conversation
chat_input.send_keys("Hello, chatbot!")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("msg")  # Replace with the actual class name of chatbot responses
print("Chatbot: " + response.text)

# Continue the conversation
chat_input.clear("hello,How can I assist you?")
chat_input.send_keys("How can I use your service?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("chatbot-response")
print("Chatbot: " + response.text)

# You can continue the conversation by repeating the steps above
# ...

# Close the browser when done
driver.quit()
