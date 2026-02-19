import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <strong>OctoFit Tracker</strong>
          </Link>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={
          <div className="container mt-5">
            <div className="jumbotron text-center">
              <h1 className="display-4">Welcome to OctoFit Tracker! 💪</h1>
              <p className="lead">Track your fitness activities, compete with teams, and achieve your goals.</p>
              <hr className="my-4" />
              <p className="mb-4">Use the navigation menu above to explore different features.</p>
              
              <div className="row mt-5">
                <div className="col-md-4 mb-3">
                  <Link to="/users" style={{textDecoration: 'none', color: 'inherit'}}>
                    <div className="card h-100 text-center" style={{cursor: 'pointer', transition: 'transform 0.2s'}} 
                         onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
                         onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}>
                      <div className="card-body">
                        <div className="mb-3" style={{fontSize: '3rem'}}>👥</div>
                        <h5 className="card-title">User Profiles</h5>
                        <p className="card-text">Manage your fitness profile with personalized metrics.</p>
                        <span className="btn btn-primary">View Users</span>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-4 mb-3">
                  <Link to="/activities" style={{textDecoration: 'none', color: 'inherit'}}>
                    <div className="card h-100 text-center" style={{cursor: 'pointer', transition: 'transform 0.2s'}}
                         onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
                         onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}>
                      <div className="card-body">
                        <div className="mb-3" style={{fontSize: '3rem'}}>🏃</div>
                        <h5 className="card-title">Track Activities</h5>
                        <p className="card-text">Log and monitor all your fitness activities.</p>
                        <span className="btn btn-success">View Activities</span>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-4 mb-3">
                  <Link to="/leaderboard" style={{textDecoration: 'none', color: 'inherit'}}>
                    <div className="card h-100 text-center" style={{cursor: 'pointer', transition: 'transform 0.2s'}}
                         onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
                         onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}>
                      <div className="card-body">
                        <div className="mb-3" style={{fontSize: '3rem'}}>🏆</div>
                        <h5 className="card-title">Leaderboard</h5>
                        <p className="card-text">Compete with others and climb the rankings.</p>
                        <span className="btn btn-warning">View Leaderboard</span>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
              
              <div className="row mt-3">
                <div className="col-md-6 mb-3">
                  <Link to="/teams" style={{textDecoration: 'none', color: 'inherit'}}>
                    <div className="card h-100 text-center" style={{cursor: 'pointer', transition: 'transform 0.2s'}}
                         onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
                         onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}>
                      <div className="card-body">
                        <div className="mb-3" style={{fontSize: '3rem'}}>👨‍👩‍👧‍👦</div>
                        <h5 className="card-title">Team Challenges</h5>
                        <p className="card-text">Join teams and compete together.</p>
                        <span className="btn btn-info">View Teams</span>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-6 mb-3">
                  <Link to="/workouts" style={{textDecoration: 'none', color: 'inherit'}}>
                    <div className="card h-100 text-center" style={{cursor: 'pointer', transition: 'transform 0.2s'}}
                         onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
                         onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}>
                      <div className="card-body">
                        <div className="mb-3" style={{fontSize: '3rem'}}>💡</div>
                        <h5 className="card-title">Workout Plans</h5>
                        <p className="card-text">Get personalized workout suggestions.</p>
                        <span className="btn btn-danger">View Workouts</span>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        } />
        <Route path="/users" element={<Users />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
