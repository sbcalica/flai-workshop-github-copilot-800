import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard:', leaderboardData);
        
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching leaderboard:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="ms-2">Loading leaderboard...</p></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger" role="alert"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Leaderboard</h2>
      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No leaderboard data found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>Rank</th>
                <th>User</th>
                <th>Total Activities</th>
                <th>Total Calories</th>
                <th>Total Distance (km)</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => (
                <tr key={entry.id || index} className={index < 3 ? 'table-warning' : ''}>
                  <td>
                    {index === 0 && <span className="badge bg-warning text-dark">🥇 1st</span>}
                    {index === 1 && <span className="badge bg-secondary">🥈 2nd</span>}
                    {index === 2 && <span className="badge bg-warning" style={{backgroundColor: '#cd7f32'}}>🥉 3rd</span>}
                    {index > 2 && <strong>{entry.rank || index + 1}</strong>}
                  </td>
                  <td><strong>{entry.user_name || entry.user}</strong></td>
                  <td>{entry.total_activities}</td>
                  <td>{entry.total_calories}</td>
                  <td>{entry.total_distance}</td>
                  <td><span className="badge bg-success fs-6">{entry.score}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
