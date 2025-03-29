import {Routes, Route, BrowserRouter, Navigate} from 'react-router-dom';
import ProtectedRoute from './components/ProtectedRoutes'
import Register from './pages/Register';
import Home from './pages/Home';
import NotFound from './pages/NotFound';
import Login from './pages/Login';

function Logout () {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout () {
  localStorage.clear()
  return <Register />
}
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<ProtectedRoute><Home /></ProtectedRoute>} />
        <Route path='/register' element={<RegisterAndLogout />} />
        <Route path='/logout' element={<Logout />} />
        <Route path='/login' element={<Login />} />
        <Route path='*' element={<NotFound />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
