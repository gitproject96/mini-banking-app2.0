from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sachin and Rupali Online Banking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background-color: #f2f2f2;
            color: #333;
        }
        /* Header */
        header {
            background-color: #003366;
            color: #fff;
            padding: 20px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        header h1 {
            margin: 0;
            font-size: 24px;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin-left: 20px;
            font-weight: bold;
        }
        nav a:hover {
            text-decoration: underline;
        }
        /* Login form */
        .login-container {
            max-width: 400px;
            margin: 50px auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #003366;
        }
        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0 20px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .login-container button {
            width: 100%;
            padding: 12px;
            background-color: #003366;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .login-container button:hover {
            background-color: #0055a5;
        }
        /* Services section */
        .services {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin: 40px;
        }
        .service-card {
            background: #fff;
            padding: 20px;
            margin: 15px;
            flex: 1 1 200px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .service-card h3 {
            color: #003366;
        }
        /* Footer */
        footer {
            background-color: #003366;
            color: #fff;
            text-align: center;
            padding: 20px;
            margin-top: 50px;
        }
    </style>
</head>
<body>

<header>
    <h1>SBI Online Banking</h1>
    <nav>
        <a href="#">Home</a>
        <a href="#">Accounts</a>
        <a href="#">Loans</a>
        <a href="#">Contact</a>
    </nav>
</header>

<div class="login-container">
    <h2>Login to Your Account</h2>
    <form>
        <input type="text" placeholder="Enter Customer ID" required>
        <input type="password" placeholder="Enter Password" required>
        <button type="submit">Login</button>
    </form>
    <p style="text-align:center; margin-top: 15px;">
        <a href="#">Forgot Password?</a> | <a href="#">Register</a>
    </p>
</div>

<section class="services">
    <div class="service-card">
        <h3>Accounts</h3>
        <p>Check your balance, view statements, and manage accounts.</p>
    </div>
    <div class="service-card">
        <h3>Loans</h3>
        <p>Apply for personal, home, or business loans online.</p>
    </div>
    <div class="service-card">
        <h3>Investments</h3>
        <p>Manage fixed deposits, mutual funds, and recurring deposits.</p>
    </div>
    <div class="service-card">
        <h3>Customer Support</h3>
        <p>Reach out to our support team for assistance anytime.</p>
    </div>
</section>

<footer>
    &copy; 2025 State Bank of India. All rights reserved. | Contact: 1800-11-2211
</footer>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
