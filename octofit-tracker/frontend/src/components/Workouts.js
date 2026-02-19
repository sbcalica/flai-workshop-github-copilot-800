import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts:', workoutsData);
        
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="ms-2">Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger" role="alert"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Workout Suggestions</h2>
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No workout suggestions found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>Workout Name</th>
                <th>Description</th>
                <th>Activity Type</th>
                <th>Duration (min)</th>
                <th>Calories</th>
                <th>Difficulty</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((workout) => (
                <tr key={workout.id}>
                  <td><strong>{workout.name}</strong></td>
                  <td>{workout.description}</td>
                  <td>{workout.activity_type}</td>
                  <td>{workout.duration}</td>
                  <td>{workout.calories_estimate}</td>
                  <td>
                    <span className={`badge ${
                      workout.difficulty === 'Hard' ? 'bg-danger' :
                      workout.difficulty === 'Medium' ? 'bg-warning' :
                      'bg-success'
                    }`}>
                      {workout.difficulty}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Workouts;
