import 'package:flutter/material.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.ac_unit_sharp,
              size: 40.0,
              color: Colors.grey,
            ),
            SizedBox(width: 8.0),
            Text(
              "Tontineo App",
              style: TextStyle(fontSize: 30.0, fontWeight: FontWeight.bold),
            ),
          ],
        ),
        centerTitle: false,
        backgroundColor: Colors.white,
        elevation: 0.0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          const Text(
            "CREATE AN ACCOUNT",
            style: TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 16.0),
          Text("Create and Manage your Tontine with ease"),

          SizedBox(height: 20.0),
          TextFormField(
            decoration: InputDecoration(
              border: const OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(5.0))),
              prefixIcon: Icon(Icons.flag, color: Colors.grey[100]),
              hintText: "Email*",
              filled: true,
              fillColor: Colors.white,
            ),
          ),
          const SizedBox(height: 20.0),
          TextFormField(
            style: TextStyle(color: Colors.green),
            decoration: InputDecoration(
              border: const OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(5.0))),
              prefixIcon: Icon(Icons.flag, color: Colors.grey[100]),
              hintText: "Phone Number*",
              filled: true,
              fillColor: Colors.white,
            ),
          ),

          // Password field
          const SizedBox(height: 20.0),
          TextFormField(
            obscureText: true,
            decoration: InputDecoration(
              border: const OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(5.0)),
              ),
              prefixIcon: Icon(Icons.lock, color: Colors.grey[100]),
              hintText: "Password*",
              filled: true,
              fillColor: Colors.white,
              suffixIcon: IconButton(
                icon: Icon(
                  Icons.visibility,
                  color: Colors.grey,
                ),
                onPressed: () {
                  // Implement the toggle visibility functionality
                },
              ),
            ),
          ),
// ...

// Text and clickable text row with checkbox
          SizedBox(height: 16.0),
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Checkbox(
                value: false, // You can manage the state of the checkbox
                onChanged: (bool? value) {
                  // Implement the logic to handle checkbox state changes
                },
              ),
              Text("Keep me logged in"),
            ],
          ),

// Register button
          SizedBox(height: 16.0),
          Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              ElevatedButton(
                onPressed: () {
                  // Implement registration functionality
                },
                style: ElevatedButton.styleFrom(
                  primary: Colors.green,
                ),
                child: const Text(
                  "Login",
                  style: TextStyle(color: Colors.white),
                  textWidthBasis: TextWidthBasis.longestLine,
                ),
              ),
            ],
          ),
          SizedBox(height: 16.0),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Don't an account"),
              SizedBox(width: 4.0),
              GestureDetector(
                onTap: () {
                  // Implement action for clickable text
                },
                child: Text(
                  "Register",
                  style: TextStyle(color: Colors.green),
                ),
              ),
            ],
          ),
        ]),
      ),
    );
  }
}
