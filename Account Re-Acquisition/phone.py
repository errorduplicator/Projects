from pywinauto import Application

# Launch or connect to the application
app = Application().start("D:\Program Files (x86)\Seewo\EasiNote5\swenlauncher\swenlauncher.exe")  # Replace with your target application

# Select the window by its title or identifier
window = app.window(title="希沃白板")  # Adjust title as needed

# Focus on the target window
window.set_focus()

# Type text into the window
window.type_keys("Hello, this is a test of pywinauto typing!", with_spaces=True)
