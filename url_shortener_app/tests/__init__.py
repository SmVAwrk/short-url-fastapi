from ..core.config import TEST_MODE

assert TEST_MODE, 'Запускать тесты необходимо в тестовом режиме в отдельной терминальной сессии ' \
                  '(export APP_TEST_MODE=1).'
