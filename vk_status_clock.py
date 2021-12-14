import vk_api
import datetime
import time

vk_session = vk_api.VkApi(login=input('VK login: '), password=input('VK password: '))
vk_session.auth()

vk = vk_session.get_api()

old_status = vk.status.get()['text'] # чтобы статус вернуть в будущем

while datetime.datetime.now().strftime('%S') != '00': # чтобы новое время отображалось в 00 секунд, а не в секунду запуска
	time.sleep(0.8)

try:
	while True:
		vk.status.set(text=f'Текущее время: {datetime.datetime.now().strftime("%H:%M")}')
		time.sleep(60)

except KeyboardInterrupt: # а вот и будущее для возврата статуса
	vk.status.set(text=old_status)