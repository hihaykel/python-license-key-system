import os
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class PremiumCompressorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("OptiPress Pro - AI Image Optimizer")
        self.geometry("900x600")
        self.resizable(False, False)

        self.selected_file_path = None
        self.original_size = 0

        # --- Main Layout Grid ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ================= LEFT PANEL (Controls) =================
        self.left_panel = ctk.CTkFrame(self, corner_radius=15)
        self.left_panel.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # App Logo / Title
        self.logo_label = ctk.CTkLabel(
            self.left_panel, 
            text="⚡ OptiPress PRO", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.logo_label.pack(pady=(30, 10), padx=20)

        self.subtitle = ctk.CTkLabel(
            self.left_panel, 
            text="Batch & High-Quality Compressor", 
            font=ctk.CTkFont(size=12), 
            text_color="gray"
        )
        self.subtitle.pack(pady=(0, 30))

        # Select Image Button
        self.btn_select = ctk.CTkButton(
            self.left_panel, 
            text="📁 Select Image", 
            height=45,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.select_image
        )
        self.btn_select.pack(pady=10, padx=20, fill="x")

        # Quality Control
        self.lbl_quality = ctk.CTkLabel(
            self.left_panel, 
            text="Compression Level: 60%", 
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_quality.pack(pady=(25, 5))

        self.slider_quality = ctk.CTkSlider(
            self.left_panel, 
            from_=10, 
            to=90, 
            number_of_steps=8,
            command=self.update_quality_label
        )
        self.slider_quality.set(60)
        self.slider_quality.pack(pady=10, padx=20, fill="x")

        # Stats Card
        self.stats_box = ctk.CTkFrame(self.left_panel, fg_color="#1E1E2E", corner_radius=10)
        self.stats_box.pack(pady=20, padx=20, fill="x")

        self.lbl_orig_size = ctk.CTkLabel(self.stats_box, text="Original: -- MB", text_color="gray")
        self.lbl_orig_size.pack(pady=(10, 2))

        self.lbl_est_size = ctk.CTkLabel(self.stats_box, text="Est. Reduced: -- MB", text_color="#2ECC71", font=ctk.CTkFont(weight="bold"))
        self.lbl_est_size.pack(pady=(2, 10))

        # Export Button
        self.btn_compress = ctk.CTkButton(
            self.left_panel, 
            text="🚀 Compress & Export", 
            height=50,
            fg_color="#27AE60", 
            hover_color="#2ECC71",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.compress_image
        )
        self.btn_compress.pack(pady=(10, 20), padx=20, fill="x", side="bottom")


        # ================= RIGHT PANEL (Preview Area) =================
        self.right_panel = ctk.CTkFrame(self, corner_radius=15, fg_color="#181825")
        self.right_panel.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")

        # Image Preview Placeholder / Image Label
        self.preview_label = ctk.CTkLabel(
            self.right_panel, 
            text="🖼️\nNo Image Loaded\nClick 'Select Image' to start", 
            font=ctk.CTkFont(size=18),
            text_color="gray"
        )
        self.preview_label.pack(expand=True, fill="both", padx=20, pady=20)

    # --- FUNCTIONS ---
    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            self.selected_file_path = file_path
            self.original_size = os.path.getsize(file_path) / (1024 * 1024) # MB
            
            # Update stats
            self.lbl_orig_size.configure(text=f"Original: {self.original_size:.2f} MB")
            self.update_estimated_size(self.slider_quality.get())

            # Render Preview Image
            img = Image.open(file_path)
            img.thumbnail((450, 450)) # Resize for UI preview
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
            
            self.preview_label.configure(image=ctk_img, text="")

    def update_quality_label(self, value):
        self.lbl_quality.configure(text=f"Compression Level: {int(value)}%")
        if self.selected_file_path:
            self.update_estimated_size(value)

    def update_estimated_size(self, quality_val):
        # Rough estimation formula for UI display
        est_size = self.original_size * (quality_val / 100.0) * 0.7
        self.lbl_est_size.configure(text=f"Est. Reduced: ~{est_size:.2f} MB")

    def compress_image(self):
        if not self.selected_file_path:
            messagebox.showwarning("Warning", "Please select an image first!")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG Image", "*.jpg")]
        )
        if not save_path:
            return

        try:
            quality_val = int(self.slider_quality.get())
            img = Image.open(self.selected_file_path)
            img = img.convert("RGB")
            img.save(save_path, "JPEG", optimize=True, quality=quality_val)
            
            saved_size = os.path.getsize(save_path) / (1024 * 1024)
            messagebox.showinfo(
                "Success", 
                f"Image saved successfully!\nOriginal: {self.original_size:.2f} MB\nNew Size: {saved_size:.2f} MB"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to compress image: {e}")

if __name__ == "__main__":
    app = PremiumCompressorApp()
    app.mainloop()