import React, { useState, useEffect } from "react";
import "./App.css";

const quotes = [
  "The only way to do great work is to love what you do. - Steve Jobs",
  "Believe you can and you're halfway there. - Theodore Roosevelt",
  "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
  "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
  // Add more quotes here
];
const about =
  "I'm Espi sharoon raj,\n A highly motivated fresher seeking for a challenging role in the field of computer science, with a particular interest in full stack development. Willing to expand into AI and WEB 3.0 in the future. My passion for technology and love for learning drives me with continuous improvement and adapt to new technologies through consistent efforts";

function App() {
  const [quoteIndex, setQuoteIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setQuoteIndex((prevIndex) => (prevIndex + 1) % quotes.length);
    }, 5000); // Change the interval duration if needed

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <div className="App">
        <header>
          <nav>
            <ul>
              <li>
                <a href="https://www.linkedin.com/in/sharoonrajespi/">
                  Linked In
                </a>
              </li>
              <li>
                <a href="https://github.com/Raju1310/personal-projects">
                  Projects Portfolio
                </a>
              </li>
              <li>
                <a href="mailto:Rajuespi13@gmail.com">Email me</a>
              </li>
            </ul>
          </nav>
        </header>
        <section id="about">
          <h1>About Me</h1>
          <p id="block">Welcome to my personal website!</p>
          {about}
        </section>
        <section id="Projects Portfolio">
          <h1>Projects Portfolio</h1>
          <a href="https://github.com/Raju1310/personal-projects">click here</a>
          <p id="inline"> to check out my projects</p>

          <p id="block">
            <h5>1.Hangman game</h5> This project is a final version of the
            classic Hangman game developed during the course of seven days.
            Guess the correct letters to reveal a hidden word before the hangman
            is fully drawn. A fun and challenging word-guessing game that tests
            your vocabulary and deduction skills.{" "}
          </p>
          <p>
            <h5>2.Snake game </h5> A rendition of the classic Snake game where
            players control a growing snake that moves around the screen. The
            objective is to eat food to grow while avoiding collisions with the
            snake's own body and the screen's boundaries. A nostalgic and
            engaging game that requires quick reflexes.
          </p>
          <p>
            <h5>3.TinDog</h5> This project is the starting point for creating a
            responsive website for a fictional dog dating app called "TinDog."
            The website showcases the app's features, testimonials, and user
            interface. An imaginative project that combines design skills with
            web development to create a visually appealing and functional app
            landing page.
          </p>
          <p>
            <h5>4. cofee machine</h5>
            An initial implementation of a coffee machine simulation. This
            project aims to replicate the process of ordering and receiving
            coffee from a coffee machine. Users can select different types of
            coffee and customize their preferences. A practical application that
            demonstrates programming logic and decision-making.{" "}
          </p>
          <p>
            <h5>5. Cipher encryptionr</h5>
            This project involves the initial implementation of an encryption
            cipher. Encryption ciphers are algorithms used to transform plain
            text into a coded version, enhancing data security. This project
            could explore various encryption techniques and their applications.
          </p>
          <p>
            <h5>6. password generator</h5>
            An initial version of a password generator tool. This project aims
            to generate strong and secure passwords based on user-defined
            parameters. A useful utility for enhancing online security by
            creating complex passwords that are harder to crack.{" "}
          </p>
          <p>
            <h5>7. pong game</h5>A recreation of the classic Pong game where two
            players control paddles on opposite sides of the screen to bounce a
            ball back and forth. This project offers a simple yet entertaining
            two-player gaming experience that harkens back to the early days of
            video games.{" "}
          </p>
          <p>
            <h5>8.quiz game</h5>
            The final version of a quiz game project that challenges users with
            a series of questions across different topics. Players select
            answers and receive feedback on their performance. A versatile
            project that combines user interaction with data processing to
            create an engaging learning experience.{" "}
          </p>
          <p>
            <h5>9.rock-paper-scissors</h5>
            The final iteration of a rock-paper-scissors game. Players choose
            between rock, paper, or scissors, and the computer makes a random
            selection. The project showcases simple game logic and randomization
            techniques while providing an interactive experience.{" "}
          </p>
          <p>
            <h5>10. Keeper App</h5>A project focused on using pre-built React
            components and libraries to develop a web application. This project
            likely explores the integration of third-party components to enhance
            functionality and streamline development, showcasing how to leverage
            existing resources to create efficient and feature-rich
            applications.
          </p>
        </section>
        <section id="contact">
          <h1>Contact Me</h1>
          <p>
            You can reach me through{" "}
            <a href="mailto:Rajuespi13@gmail.com">email</a>
          </p>
        </section>
      </div>{" "}
      <section id="inspiration">
        <div className="quote-container">
          <h2>Inspiration for You</h2>
          <p className="quote">{quotes[quoteIndex]}</p>
        </div>
      </section>
      <footer>
        <p>&copy; 2023 Raju Espi. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
