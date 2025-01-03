import React, { useState, useEffect } from "react";
import axios from "axios";
import { useCookies } from "react-cookie"; // To get cookies
import { useNavigate } from "react-router-dom"; // To navigate back
import { FaMapMarkedAlt } from "react-icons/fa"; // Map icon for full-screen map view
import './Play.css'; // Assuming you have a CSS file for styling

const Play = () => {
  const [action, setAction] = useState(""); // For user action input
  const [gameState, setGameState] = useState(null); // Store game state (current room, etc.)
  const [response, setResponse] = useState(""); // Store game responses like room descriptions and action results
  const [isGameStarted, setIsGameStarted] = useState(false); // Flag for game start
  const [showMapImage, setShowMapImage] = useState(false); // Toggle for full-screen map preview
  const [cookies] = useCookies(["accountDetails"]); // To get account details from cookies
  const navigate = useNavigate(); // To navigate to different pages
  const [roomImage, setRoomImage] = useState(""); // Store image url for the room


  // Get accountId from cookies
  const accountId = cookies.accountDetails?.accountid;

  useEffect(() => {
    if (!accountId) {
      navigate("/"); // Redirect if no account ID in cookies
    }
  }, [accountId, navigate]);

  // Start a new game
  const startGame = async () => {
    if (!accountId) {
      alert("Account ID is missing. Please log in.");
      return;
    }

    try {
      const res = await axios.post("/api/start_game", { accountId });
      setGameState(res.data.state);
      setResponse(res.data.message);
      setIsGameStarted(true);
    } catch (error) {
      console.error("Error starting game:", error);
      setResponse("Error starting the game. Try again.");
    }
  };

  // Load an existing game
  const loadGame = async () => {
    if (!accountId) {
      alert("Account ID is missing. Please log in.");
      return;
    }

    try {
      const res = await axios.post("/api/load_game", { accountId });
      setGameState(res.data.state);
      setResponse(res.data.message);
      setIsGameStarted(true);
    } catch (error) {
      console.error("Error loading game:", error);
      setResponse("No saved game found for this account.");
    }
  };

  // Handle user actions like 'look around', 'go north', etc.
  const handleAction = async () => {
    if (!action) {
      alert("Please enter an action.");
      return;
    }

    try {
      const res = await axios.post("/api/perform_action", {
        accountId,
        action,
      });
      setGameState(res.data.state);
      setResponse(res.data.message);

      if (res.data.roomImageurl) {
        setRoomImage(`${res.data.roomImageurl}`);
        console.log(roomImage);

      }
       // Display the result (e.g., action result, updated room description)
      setAction(""); // Clear the action input field
    } catch (error) {
      console.error("Error performing action:", error);
      setResponse("Error processing the action. Try Loading or Starting a new Game. ");
    }
  };

  // Save the game state
  const saveGame = async () => {
    try {
      const res = await axios.post("/api/save_game", { accountId });
      setResponse(res.data.message); // Display save success message
    } catch (error) {
      console.error("Error saving game:", error);
      setResponse("Error saving the game. Try Loading or Starting a new Game.");
    }
  };

  // Exit the game and save the state
  const exitGame = async () => {
    try {
      const res = await axios.post("/api/exit_game", { accountId });
      setResponse(res.data.message); // Display exit and save message
      setIsGameStarted(false); // End the game session
      setGameState(null); // Clear the game state
    } catch (error) {
      console.error("Error exiting game:", error);
      setResponse("Error exiting the game. Try again.");
    }
    finally{
      navigate("/"); // Navigate back to the home page
    }
  };

  // Handle back button click (combined with exit)
  const handleBack = () => {
    exitGame(); // Exit the game before navigating back
  };

  // Handle Enter key press to submit action
  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleAction(); // Call handleAction when Enter is pressed
    }
  };

  return (
    <div className="play-page">
      <div className="crt-container">
        {/* Exit Game Button (combined with back) */}
        <button className="back-button" onClick={handleBack}>
          Exit
        </button>

        {/* Room Image Display */}
        <div className="image-display">
        <img
          src={
            roomImage && (roomImage.startsWith('http') || roomImage.startsWith('https'))
              ? roomImage
              : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAwAB/9TgZmkAAAAASUVORK5CYII="
          }
          alt="Room"
          className="play-image"
        />
        </div>

        {/* Display Text Section */}
        <div className="display-text-container">
          <div className="text-display">
            <p className="play-text">{response || ""}</p>
          </div>
        </div>

        {/* Map Icon Display */}
        <div className="map-icon-container" onClick={() => setShowMapImage(true)}>
          <FaMapMarkedAlt className="map-icon" />
          <p>Map</p>
        </div>

        {/* Full-screen Map Preview */}
        {showMapImage && (
          <div className="map-overlay" onClick={() => setShowMapImage(false)}>
            <img src="/images/logos/map.png" alt="Map Full View" className="map-fullscreen" />
          </div>
        )}

        {/* Input Text Section for Actions */}
        <div className="input-text-container">
          <input
            type="text"
            value={action}
            onChange={(e) => setAction(e.target.value)}
            placeholder="Enter your action (e.g., 'look around')"
            className="text-input"
            onKeyDown={handleKeyDown} // Attach the onKeyDown event handler
          />
        </div>

        {/* Action Buttons */}
        <div className="action-buttons">
          {!isGameStarted && (
            <>
              <button onClick={startGame}>🎮 New Game</button>
              <button onClick={loadGame}>📂 Load Game</button>
            </>
          )}

          {isGameStarted && (
            <button onClick={saveGame}>💾 Save</button>
          )}
        </div>
      </div>
    </div>
  );
};

export default Play;
