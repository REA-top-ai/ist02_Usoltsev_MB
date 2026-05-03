# # 1. Проверить версии
# pip show fastapi starlette jinja2
#
# # 2. Убедиться, что starlette официальный
# #    ✅ https://github.com/encode/starlette
# #    ❌ https://github.com/Kludex/starlette
#
# # 3. Очистить кэш
# Get-ChildItem -Recurse -Filter __pycache__ | Remove-Item -Recurse -Force
#
# # 4. Перезапустить сервер ПОЛНОСТЬЮ (убить процесс python.exe)
#
# # 5. Проверить тип кэша
# python -c "from app import templates; print(type(templates.env.cache))"
# # Должно быть: <class 'jinja2.utils.LRUCache'>