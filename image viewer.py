import tkinter as tk
from PIL import Image, ImageTk

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ImageViewer:
    def __init__(self):
        self.head = None
        self.current = None

    def add_image(self, image_path):
        new_node = Node(image_path)
        if self.head is None:
            self.head = new_node
            self.current = new_node
        else:
            self.current.next = new_node
            self.current = new_node

    def display_current_image(self):
        if self.current:
            print("Currently viewing:", self.current.data)
        else:
            print("No image to display.")

    def next_image(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print("Moving to next image.")
            self.display_current_image()
        else:
            print("No next image available.")

    def prev_image(self):
        if self.current == self.head:
            print("No previous image available.")
        else:
            prev_node = self.head
            while prev_node.next != self.current:
                prev_node = prev_node.next
            self.current = prev_node
            print("Moving to previous image.")
            self.display_current_image()

    def delete_current_image(self):
        if self.current == self.head:
            self.head = self.head.next
            self.current = self.head
            print("Deleted current image.")
        else:
            prev_node = self.head
            while prev_node.next != self.current:
                prev_node = prev_node.next
            prev_node.next = self.current.next
            self.current = prev_node.next
            print("Deleted current image.")

class ImageViewerGUI:
    def __init__(self, master):
        self.master = master
        self.viewer = ImageViewer()

        self.label = tk.Label(master)
        self.label.pack()

        self.prev_button = tk.Button(master, text="Previous", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(master, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_image)
        self.delete_button.pack()

        
        
        
        self.viewer.add_image("C:\\Users\91974\\Downloads\\iloveimg-resized\\stadium (1).jpg")
        self.viewer.add_image("C:\\Users\91974\\Downloads\\iloveimg-resized\\stadium (2).jpg")
        self.viewer.add_image("C:\\Users\91974\\Downloads\\iloveimg-resized\\stadium (3).jpg")
        self.viewer.add_image("C:\\Users\91974\\Downloads\\iloveimg-resized\\stadium (4).jpg")
        self.viewer.add_image("C:\\Users\91974\\Downloads\\iloveimg-resized\\stadium (5).jpg")
        self.viewer.add_image("C:\\Users\91974\\Downloads\\iloveimg-resized\\stadium (6).jpg")
     
        self.display_current_image()

    def display_current_image(self):
        if self.viewer.current:
            image = Image.open(self.viewer.current.data)
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo
        else:
            self.label.config(image=None)

    def next_image(self):
        self.viewer.next_image()
        self.display_current_image()

    def prev_image(self):
        self.viewer.prev_image()
        self.display_current_image()

    def delete_image(self):
        self.viewer.delete_current_image()
        self.display_current_image()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Viewer")
    app = ImageViewerGUI(root)
    root.mainloop()