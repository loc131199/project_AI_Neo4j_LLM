import os
from dotenv import load_dotenv

# Nạp biến môi trường từ file .env khi chạy local (không bắt buộc trên Render)
load_dotenv(dotenv_path="backend/.env")

# --- Cấu hình Neo4j AuraDB ---
NEO4J_URI = os.getenv("NEO4J_URI", "")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")

# --- Cấu hình OpenAI ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# Model LLM (có thể đổi sang "gpt-4o" hoặc biến môi trường MODEL_LLM)
MODEL_LLM = os.getenv("MODEL_LLM", "gpt-4o")

# # Nếu sau này bạn có dùng embedding để tìm kiếm ngữ cảnh:
# MODEL_EMBEDDING = "text-embedding-3-small"  # hoặc "text-embedding-3-large"
# import os
# from dotenv import load_dotenv

# # Nạp biến môi trường từ file .env (chỉ khi chạy local)
# load_dotenv(dotenv_path="backend/.env")

# # Đọc API key từ biến môi trường
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # Kiểm tra API key có tồn tại không
# if not OPENAI_API_KEY:
#     raise ValueError("⚠️ OPENAI_API_KEY chưa được cấu hình. "
#                      "Hãy tạo file .env và thêm OPENAI_API_KEY=your_key_here")






