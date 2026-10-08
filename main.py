import platform

def main():
    print("Hello from GitHub Release Demo!")
    print(f"当前系统: {platform.system()} {platform.release()}")
    print(f"架构: {platform.machine()}")

if __name__ == "__main__":
    main()