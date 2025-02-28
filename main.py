"from flask import Flask, render_template_string
app = Flask(__name__)
# HTML template as a multi-line string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Services - Black Alliance</title>
 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
 <style>
  :root{
   --background-image-url: url('/static/images/bg.jpg');
  }
 </style>
 <link rel="stylesheet" href="/static/css/main.css">
 <link rel="stylesheet" href="/static/css/animation.css">
</head>
<body>
 <nav class="navbar p-4 shadow-md">
  <div class="container mx-auto flex justify-between items-center">
   <div class="text-2xl text-primary">Black Alliance ♚</div>
   <div class="hidden lg:flex navbar-menu">
    <a href="/" class="hover:text-primary">Home</a>
    <a href="/team" class="hover:text-primary">Team</a>
    <a href="/services" class="hover:text-primary">Services</a>
    <a href="/status" class="hover:text-primary">Status</a>
    <a href="/pricing" class="hover:text-primary">Pricing</a>
    <a href="/contact" class="hover:text-primary">Contact</a>
   </div>
   <div class="lg:hidden">
    <span id="menu-btn" class="navbar-icon text-2xl">
     <i class="fas fa-bars"></i>
    </span>
   </div>
  </div>
 </nav>
 <div id="sidebar" class="fixed inset-0 bg-white text-gray-800 lg:hidden">
  <div class="w-64 h-full p-4">
   <ul class="space-y-6">
    <li><a href="/" class="hover:text-primary">Home</a></li>
    <li><a href="/team" class="hover:text-primary">Team</a></li>
    <li><a href="/services" class="hover:text-primary">Services</a></li>
    <li><a href="/status" class="hover:text-primary">Status</a></li>
    <li><a href="/pricing" class="hover:text-primary">Pricing</a></li>
    <li><a href="/contact" class="hover:text-primary">Contact</a></li>
   </ul>
  </div>
 </div>
 <header class="bg-header shadow-lg flex items-center justify-center text-center"></header>
 <div class="container mx-auto px-4 py-16">
  <section id="cards">
   <h2 class="text-3xl font-bold text-center text-primary mb-8">Our Services</h2>
   <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    {services}
   </div>
  </section>
 </div>
 <footer class="footer py-6">
  <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
   <div class="mb-4 md:mb-0">
    <a href="/terms" class="hover:text-primary">Terms</a>
    <span class="mx-2">|</span>
    <a href="/privacy" class="hover:text-primary">Privacy</a>
   </div>
   <div name="links" class="flex space-x-4">
    <a href="https://www.facebook.com/Mr.Raja6970" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
    <a href="https://wa.me/+923040176170" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
    <a href="https://github.com" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a"
 https://chat.two.ai/#:~:text=Python%20Flask%20Script-,from,-flask
