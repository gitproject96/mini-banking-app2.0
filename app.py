from flask import Flask, render_template_string
import os

app = Flask(__name__)

# You can pass the version via environment variable
APP_VERSION = os.getenv("APP_VERSION", "v0.0.0")

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HDFC Bank - Home</title>
    <style>
        /* Reset some defaults */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }

        /* Header */
        header {
            background-color: #004b87; /* HDFC Blue */
            color: white;
            padding: 15px 50px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        header h1 {
            font-size: 24px;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
            font-weight: bold;
        }

        nav a:hover {
            text-decoration: underline;
        }

        /* Hero Section */
        .hero {
            background-image: url('https://images.unsplash.com/photo-1581092334703-3fc0b10395a5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218fHx8fHx8fHwxNjk2NzQ4NzA5&ixlib=rb-4.0.3&q=80&w=1400');
            background-size: cover;
            background-position: center;
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
        }

        .hero h2 {
            font-size: 36px;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 8px;
        }

        /* Services Section */
        .services {
            display: flex;
            justify-content: space-around;
            padding: 50px 20px;
            background-color: #ffffff;
        }

        .service-card {
            background-color: #f1f1f1;
            padding: 20px;
            width: 250px;
            text-align: center;
            border-radius: 8px;
            transition: transform 0.3s;
        }

        .service-card:hover {
            transform: scale(1.05);
        }

        .service-card h3 {
            color: #004b87;
            margin-bottom: 10px;
        }

        /* Footer */
        footer {
            background-color: #004b87;
            color: white;
            padding: 20px 50px;
            text-align: center;
        }

        footer a {
            color: #f8f9fa;
            margin: 0 10px;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .services {
                flex-direction: column;
                align-items: center;
            }

            .service-card {
                margin-bottom: 20px;
            }

            header {
                flex-direction: column;
                align-items: flex-start;
            }

            nav {
                margin-top: 10px;
            }
        }
    </style>
</head>
<body>

    <header>
        <h1>HDFC Bank</h1>
        <nav>
            <a href="#">Home</a>
            <a href="#">Accounts</a>
            <a href="#">Loans</a>
            <a href="#">Cards</a>
            <a href="#">NetBanking</a>
            <a href="#">Contact</a>
        </nav>
    </header>

    <section class="hero">
        <h2>Banking Made Simple and Secure</h2>
    </section>

    <section class="services">
        <div class="service-card">
            <h3>Savings Account</h3>
            <p>Open a savings account with competitive interest rates.</p>
        </div>
        <div class="service-card">
            <h3>Personal Loans</h3>
            <p>Flexible personal loans to meet your financial needs.</p>
        </div>
        <div class="service-card">
            <h3>Credit Cards</h3>
            <p>Choose from a range of credit cards with rewards.</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2025 HDFC Bank. All Rights Reserved.</p>
        <div>
            <a href="#">Privacy Policy</a> |
            <a href="#">Terms & Conditions</a> |
            <a href="#">Help</a>
        </div>
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

