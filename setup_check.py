"""
Quick Setup and Validation Script
Kiểm tra environment và chạy quick test
"""

import subprocess
import sys
import os
import importlib.util


def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required")
        return False
    
    print("✅ Python version OK")
    return True


def check_cuda():
    """Check CUDA availability"""
    try:
        import torch
        if torch.cuda.is_available():
            device_name = torch.cuda.get_device_name()
            print(f"🚀 CUDA available: {device_name}")
            print(f"🔥 GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
            return True
        else:
            print("⚠️  CUDA not available - will use CPU (slower)")
            return False
    except ImportError:
        print("❌ PyTorch not installed")
        return False


def install_requirements():
    """Install requirements"""
    print("📦 Installing requirements...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False


def check_files():
    """Check required files exist"""
    required_files = [
        "answer_template.md",
        "question.csv", 
        "true_result.md",
        "main.py",
        "rag_system.py",
        "mcq_processor.py"
    ]
    
    missing = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing.append(file)
    
    return len(missing) == 0


def test_imports():
    """Test critical imports"""
    imports_to_test = [
        ("torch", "PyTorch"),
        ("transformers", "Transformers"),
        ("llama_index", "LlamaIndex"),
        ("chromadb", "ChromaDB"),
        ("pandas", "Pandas")
    ]
    
    failed = []
    for module, name in imports_to_test:
        try:
            importlib.import_module(module)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} - IMPORT FAILED")
            failed.append(name)
    
    return len(failed) == 0


def main():
    """Main setup validation"""
    print("="*60)
    print("🔧 Vietnamese MCQ RAG System - Setup Validation")
    print("="*60)
    
    # Check Python
    if not check_python_version():
        return 1
    
    print("\n📦 Checking dependencies...")
    
    # Install requirements if needed
    if not test_imports():
        print("\n🔄 Installing missing dependencies...")
        if not install_requirements():
            return 1
        
        # Test again
        print("\n🔄 Re-testing imports...")
        if not test_imports():
            print("❌ Some imports still failing")
            return 1
    
    print("\n🔧 Checking hardware...")
    check_cuda()
    
    print("\n📁 Checking files...")
    if not check_files():
        print("❌ Missing required files")
        return 1
    
    print("\n" + "="*60)
    print("✅ Setup validation completed successfully!")
    print("🚀 Ready to run: python main.py evaluate")
    print("="*60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())