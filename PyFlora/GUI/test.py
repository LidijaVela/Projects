main_frame = Frame(my_window)
main_frame.grid(row=0, column=0, sticky="nswe")

left_frame = Frame(main_frame)
left_frame.grid(row=0, column=0, sticky="nswe")

# Button added just to see that there is a left frame, otherwise it will shrink
button_object = Button(left_frame, text="My Button")
button_object.grid(row=0, column=0)

right_frame = Frame(main_frame)
right_frame.grid(row=0, column=1, sticky="nswe")

listbox_object = Listbox(right_frame)
listbox_object2 = Listbox(right_frame)
listbox_object.grid(row=0, column=0)
listbox_object2.grid(row=0, column=2)

scrollbar_object = Scrollbar(right_frame)
scrollbar_object2 = Scrollbar(right_frame)
scrollbar_object.grid(row=0, column=1, sticky='ns')
scrollbar_object2.grid(row=0, column=3, sticky='ns')