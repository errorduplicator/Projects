from pywinauto import Application
from pywinauto.keyboard import send_keys

app = Application(backend='uia').connect(best_match="希沃白板")
window = app.top_window()
edit_control_1 = window.child_window(control_type="Edit", found_index=0)
edit_control_2 = window.child_window(control_type="Edit", found_index=1)

file = open("log.txt", "a")

for i in range(2):
    # Generate a string based on the value of i: "89" when i is 1, "98" when i is 0
    series_1 = str(59 * i + 95 * int(not i))
    for j in range(4):
        series_2_values = ["45", "54", "85", "58"]
        series_2 = series_2_values[j]
        for k in range(2):
            series_3 = str(k)
            phone = "151" + series_1 + series_2 + "275" + series_3
            # Focus on the first input box
            edit_control_1.set_focus()
            # Clear the first input box
            send_keys('^a{DELETE}')
            # Enter the phone number
            send_keys(phone)
            for pa in range(2):
                # Focus on the second input box
                edit_control_2.set_focus()
                # Clear the second input box
                send_keys('^a{DELETE}')
                # Generate a string based on the value of i: "89" when i is 1, "98" when i is 0
                password = 'lnl98' + str(0 * pa + 6 * int(not pa))
                send_keys(password)
                send_keys("{ENTER}")
                file.write(f"Phone: {phone}, Password: {password}\n")
file.close()