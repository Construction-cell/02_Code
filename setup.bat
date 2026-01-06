@echo off
echo 智能小车环境一键恢复
echo.

echo 1. 清理旧环境...
rmdir /s /q .venv 2>nul
rmdir /s /q __pycache__ 2>nul
del /q *.pyc 2>nul

echo 2. 创建新环境...
python -m venv .venv --clear

echo 3. 激活环境...
call .venv\Scripts\activate

echo 4. 安装核心库...
pip install numpy==1.24.3 -i https://mirrors.aliyun.com/pypi/simple/
pip install opencv-python==4.8.1.78 -i https://mirrors.aliyun.com/pypi/simple/
pip install pyserial==3.5 -i https://mirrors.aliyun.com/pypi/simple/

echo 5. 验证安装...
python test_env.py

echo.
echo ========================================
echo 环境搭建完成！
echo ========================================
pause