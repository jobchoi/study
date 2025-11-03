import tensorflow as tf

# GPU 장치가 보이는지 확인합니다.
gpu_list = tf.config.list_physical_devices('GPU')
print(gpu_list)

if gpu_list:
    print("✅ 🚀 GPU가 성공적으로 인식되었습니다. 🚀 ✅")
else:
    print("❌ 💻 GPU가 인식되지 않았습니다. CPU 모드로 동작합니다. 💻 ❌")