import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

rate = robot_mouth.getProperty('rate')
robot_mouth.setProperty('rate', 135)
robot_mouth.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_viVN_An')
volume = robot_mouth.getProperty('volume')
robot_mouth.setProperty('volume', 1.0) 

while True:
	with speech_recognition.Microphone() as mic:
		robot_ear.adjust_for_ambient_noise(mic)
		print("Robot: Tôi đang nghe...")
		audio =robot_ear.record(mic, duration=5)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio, language="vi")
	except:
		you = ""

	print("You: " + you)

	if you == "":
		robot_brain = "Tôi không thể nghe bạn nói, hãy thử lại "
	elif "ngày" in you:
		today = date.today()
		robot_brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y")
	elif "giờ" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H:%M:%S")
	elif "tổng thống" in you:
		robot_brain = "Joe Biden là tổng thống Mỹ"
	elif "bye" in you or "tạm biệt" in you:
		robot_brain = "Chào Mai Toàn đẹp trai"
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	elif "hello" in you or "chào" in you:
		robot_brain = "Chào Mai Toàn đẹp trai"
	else:
		robot_brain = "Tôi ổn, còn bạn"

	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()