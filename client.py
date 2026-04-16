import socket
import json
import time

def test_connection(host, port):
    print(f"🔌 Тестирование подключения к {host}:{port}")
    
    try:
        # Создаем сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        print("⏳ Подключение...")
        sock.connect((host, port))
        print("✅ Подключено!")
        
        # Отправляем тестовый логин
        login_data = json.dumps({'type': 'login', 'name': 'TestUser'})
        print(f"📤 Отправка: {login_data}")
        sock.send(login_data.encode('utf-8'))
        
        # Ждем ответ
        print("⏳ Ожидание ответа...")
        response = sock.recv(4096).decode('utf-8')
        print(f"📨 Ответ сервера: {response}")
        
        # Парсим JSON
        data = json.loads(response)
        print(f"✅ Ответ успешно распарсен: {data}")
        
        sock.close()
        print("✅ Тест пройден успешно!")
        return True
        
    except socket.timeout:
        print("❌ Таймаут подключения")
        return False
    except ConnectionRefusedError:
        print("❌ Сервер отклонил подключение")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

if __name__ == "__main__":
    # ЗАМЕНИТЕ НА ВАШ АДРЕС ОТ RAILWAY
    HOST = "xxx.proxy.rlwy.net"  # Например: modern-chat.proxy.rlwy.net
    PORT = 12345  # Порт от Railway (обычно 5 цифр)
    
    print("=" * 50)
    print("ТЕСТ ПОДКЛЮЧЕНИЯ К ЧАТ-СЕРВЕРУ")
    print("=" * 50)
    
    result = test_connection(HOST, PORT)
    
    if result:
        print("\n🎉 Подключение работает! Проблема в клиенте.")
    else:
        print("\n❌ Подключение не работает. Проверьте:")
        print("1. Запущен ли сервер на Railway")
        print("2. Правильный ли адрес и порт")
        print("3. Включен ли TCP Proxy в настройках Railway")
    
    input("\nНажмите Enter для выхода...")