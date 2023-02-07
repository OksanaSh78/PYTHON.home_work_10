from aiogram import executor
from handlers import dp 

async def on_start(_):                  # async - запрос возвращается, а программа работает дальше  
    print('Бот запущен')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)       # если поставить False, то сообщения будут 
                                                                         # попадать в ожидание и накапливаться, пока не поменяем на True


#from aiogram import executor
#from handlers import dp


#async def on_start(_):
#    print('Бот запущен')


#executor.start_polling(dp, skip_updates=True, on_startup=on_start)                                                                         