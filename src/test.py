from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

# Open the chatbot webpage
driver.get("https://khaanvaani.streamlit.app/")  # Replace with the URL of the chatbot

# Find the chat input element by class name
chat_input = driver.find_element_by_class_name("st-ai")  # Replace with the actual class name of the chat input field

# Start a conversation
chat_input.send_keys("How can I assist you?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("msg")  # Replace with the actual class name of chatbot responses
print("Chatbot: " + response.text)

# Continue the conversation
chat_input.clear()
chat_input.send_keys("I had an accident in a mining site. What should I do?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("msg")
print("Chatbot: " + response.text)

# You can continue the conversation by repeating the steps above
# ...

# Close the browser when done
driver.quit()
