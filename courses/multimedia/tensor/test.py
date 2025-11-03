import tensorflow as tf
print(f"TensorFlow Version: {tf.__version__}")

# GPU 확인 코드 (CPU면 빈 리스트가 정상)
gpu_list = tf.config.list_physical_devices('GPU')
if gpu_list:
    print("✅ 🚀 GPU가 성공적으로 인식되었습니다. 🚀 ✅")
else:
    print("❌ 💻 GPU가 인식되지 않았습니다. CPU 모드로 동작합니다. 💻 ❌")