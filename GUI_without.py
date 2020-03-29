import tkinter as tk
import os
import jsonlines as jsnl
from PIL.ImageTk import PhotoImage

from visualizer import Visualizer
import pickle


def get_img_file(root_name):
    """get all image file, return a sorted list"""
    img_list = []
    for root, dirnames, filenames in os.walk(root_name):
        for filename in filenames:
            if filename.lower().endswith(
                    ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                img_list.append(os.path.join(filename))
                img_list.sort(key=lambda x: int(x[:6]))
        return img_list


def center_window(weight, height):
    # 获取屏幕 宽、高
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (weight / 2)
    y = (hs / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (weight, height, x, y))




def vp_start_gui():

    global window
    global i
    global my_image_number
    global var

    if i > 99:
        exit()

    def print_selection():
        if var.get() == 0:
            l1.config(text='You have selected A')
        elif var.get() == 1:
            l1.config(text='You have selected B')
        elif var.get() == 2:
            l1.config(text='You have selected C')
        else:
            l1.config(text='You have selected D')

    def save_answer():
        global chosen       # start len 0
        global i   # start at 1
        global var
        if len(chosen) > i-1:
            chosen.pop()
        chosen.append(var.get())
        #print('new', chosen)
        if i > 0:
            pickle_file = open('chosen.pickle', 'wb')
            pickle.dump(chosen, pickle_file)
            pickle_file.close()

    def show_hide():
        global my_image_number
        my_image_number += 1
        # return to first image
        if my_image_number == len(my_images):
            my_image_number = 0
        # change image
        canvas.itemconfig(image_on_canvas, image=my_images[my_image_number])

    # def resize(w_box, h_box, image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
    #     w = image.width()  # 获取图像的原始大小
    #     h = image.height()
    #     f1 = 1.0 * w_box / w
    #     f2 = 1.0 * h_box / h
    #     factor = min([f1, f2])
    #     width = int(w * factor)
    #     height = int(h * factor)
    #     image = ImageTk.PhotoImage(image)
    #     return image.resize((width, height), Image.ANTIALIAS)

    window = tk.Tk()
    window.title('VCR Human Performance')
    #window.config(bg='turquoise1')
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    #center_window(ws/1.5, hs/1.5)
    center_window(2500, 1400)
    img_list = get_img_file('images')
    img_name = 'images/' + img_list[i]
    file_name = os.path.splitext(img_name)[0]
    dict_data_file = file_name + '.jsonl'
    meta_data_file = file_name + '.json'
    img_data_file = file_name + '.jpg'
    mask_image = file_name + '.gif'
    val_annots = jsnl.Reader(open(dict_data_file))
    chosen = []
    t1 = []
    for t in val_annots.iter():
        t1.append(t)
    anno = t1[0]
    vis = Visualizer(meta_data_file, anno, img_data_file)
    # ori_img, mask_img = vis.get_img(), vis.get_mask_ann_img()
    dct = vis.get_qar()

    my_images = [PhotoImage(file=img_data_file), PhotoImage(file=mask_image)]

    # w = Image.open(my_images[my_image_number]) #.width()
    # a=1
    # b=3

    canvas = tk.Canvas(window, width=2000, height=1200)

    # w_box = 700             # 期望图像显示的大小（窗口大小）
    # h_box = 100
    # #image_resized = resize(w_box, h_box, my_images[my_image_number])
    # #tk_image = ImageTk.PhotoImage(image_resized)



    #h = my_images[my_image_number].height()
    image_on_canvas = canvas.create_image(1000, 0, anchor='n', image=my_images[my_image_number])
#   image_on_canvas = canvas.create_image(1000, 0, anchor='n', image=tk_image)
    canvas.pack()




    """ INSERT YOUR WHOLE CODE HERE"""
    """ CREATE A BUTTON AND ITS command = refresh() which is defined at the bottom"""

    b1 = tk.Button(window, text='next', font=('Arial', 16), width=10, height=2, command=refresh)
    b1.place(relx=0.94, rely=0.96, anchor='center', width=120, height=50)

    # b2 = tk.Button(window, text='save', bg='red', font=('Arial', 16), width=10, height=2, command=save_answer)
    # b2.place(relx=0.4, rely=0.95, anchor='center', width=120, height=50)

    b3 = tk.Button(window, text='Hide/Show', bg='DarkOrange', font=('Arial', 16), width=10, height=2, command=show_hide)
    b3.place(relx=0.06, rely=0.96, anchor='center', width=120, height=50)

    var = tk.IntVar()
    l1 = tk.Label(window, bg='turquoise1', width=20, height=1, font=('Arial', 20), text=None)
    l1.place(relx=0.98, rely=0.93, anchor='e')

    l2 = tk.Label(window, bg='LightPink', font=('Arial', 20), text='Answer: ' + dct['answer_choices'][dct['answer_label']])
    l2.place(relx=0.09, rely=0.96, anchor='w')

    r1 = tk.Radiobutton(window, text='A: ' + dct['rationale_choices'][0], font=('Arial', 15), height=1, variable=var,
                        value=0, command=print_selection)
    r1.place(relx=0.0, rely=0.81, anchor='w')
    r2 = tk.Radiobutton(window, text='B: ' + dct['rationale_choices'][1], font=('Arial', 15), height=1, variable=var,
                        value=1, command=print_selection)
    r2.place(relx=0.0, rely=0.84, anchor='w')
    r3 = tk.Radiobutton(window, text='C: ' + dct['rationale_choices'][2], font=('Arial', 15), height=1, variable=var,
                        value=2, command=print_selection)
    r3.place(relx=0.0, rely=0.87, anchor='w')
    r4 = tk.Radiobutton(window, text='D: ' + dct['rationale_choices'][3], font=('Arial', 15), height=1, variable=var,
                        value=3, command=print_selection)
    r4.place(relx=0.0, rely=0.9, anchor='w')

    i += 1

    window.mainloop()


if __name__ == '__main__':
    def refresh():
        global chosen       # start len 0
        global i   # start at 1
        global var

        if len(chosen) > i-1:
            chosen.pop()
        chosen.append(var.get())

        if i > 0:
            pickle_file = open('chosen.pickle', 'wb')
            pickle.dump(chosen, pickle_file)
            pickle_file.close()
        # if len(chosen) != i:
        #     tk.messagebox.showwarning(title='Hi', message='别忘了保存')
        #     return
        window.destroy()
        vp_start_gui()

    if os.path.exists('chosen.pickle'):
        with open('chosen.pickle', 'rb') as cfile:
            a_dict1 = pickle.load(cfile)
        i = len(a_dict1)
        my_image_number = 0
        chosen = a_dict1
        vp_start_gui()
    else:
        i = 0
        my_image_number = 0
        chosen = []
        vp_start_gui()


