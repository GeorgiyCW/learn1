from datetime import datetime, timedelta

  data_now = datetime.now()
  data_yesterday = data_now - timedelta(days=1)
  month_ago = int(data_now.strftime('%m')) - 1

  print('Вчера: {}'.format(data_yesterday.date()))
  print('Сегодня: {}'.format(data_now.date()))
  print(data_now.strftime('Месяц назад: %Y-{}-%d').format(month_ago))


date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f')
print(date_dt)
