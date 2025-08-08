# 创建事项
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"First Todo"}'

# 获取所有事项
curl http://localhost:5000/todos
