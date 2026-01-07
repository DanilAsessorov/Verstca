#!/usr/bin/env python3
"""
Простое веб-приложение без фреймворков.
На любой GET-запрос возвращает страницу "Контакты".
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обработка GET-запросов"""
        try:
            # Чтение HTML-файла
            with open('templates/contacts.html', 'r', encoding='utf-8') as file:
                content = file.read()

            # Отправка ответа
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))

        except FileNotFoundError:
            self.send_error(404, "Файл не найден")
        except Exception as e:
            self.send_error(500, f"Ошибка сервера: {str(e)}")

    def log_message(self, format, *args):
        """Отключение логов для чистоты вывода"""
        pass


def run_server(port=8000):
    """Запуск HTTP-сервера"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f'Сервер запущен на порту {port}')
    print('Откройте http://localhost:8000 в браузере')
    print('Нажмите Ctrl+C для остановки сервера')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nСервер остановлен')


if __name__ == '__main__':
    run_server()