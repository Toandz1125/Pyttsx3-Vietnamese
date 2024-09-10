import pyttsx3

robot_brain = "xin chào Mai Toàn đẹp trai"

robot_mouth = pyttsx3.init()
rate = robot_mouth.getProperty('rate')
robot_mouth.setProperty('rate', 135)  # Đặt tốc độ mới
#c1:dat giong noi moi
# robot_mouth.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
#c2:dat giong noi moi
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

    # kiểm tra id giọng nói.
# voices = robot_mouth.getProperty('voices')

# for voice in voices:
#     print(f"Voice ID: {voice.id}, Name: {voice.name}, Gender: {voice.gender}") 

# Thay đổi âm lượng 0:min 1:max
volume = robot_mouth.getProperty('volume')
robot_mouth.setProperty('volume', 1.0) 