import dearpygui.dearpygui as dpg

def convert(user_data):
    print("Clicked!")
    print(user_data)



def main():
    dpg.create_context()

    with dpg.window(tag="Primary Window", label="Ru's Converter"):
        dpg.add_text("Welcome to Ru's Converter!")
        
        with dpg.group() as converting_table:
            input = dpg.add_input_float(label="Input")
            dpg.add_button(label="Convert", callback=convert, user_data=input)
        
        dpg.add_text("\n")
        
        with dpg.group() as conversion_values:
            cm = input * 10
            dm = input * 100
            mm = input * 1000
            cm_txt = dpg.add_text(cm)
            dm_txt = dpg.add_text(dm)
            m_txt = dpg.add_text(mm)



    vp_width = 800
    vp_height = 500

    dpg.create_viewport(
        title="Main Page", 
        width=vp_width, 
        height=vp_height
    )
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    
    dpg.start_dearpygui()
    dpg.destroy_context()
    
main()