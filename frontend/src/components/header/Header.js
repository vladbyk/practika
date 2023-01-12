import './Header.css'
import {Link, NavLink} from "react-router-dom";
import logo from './logo.png'

function Header() {
  const exitHundler = () =>{
    sessionStorage.clear()
    window.location.assign('/login')
  }
  return (
    <nav>
        <p><NavLink to='/'><img src={logo} alt='logo'/></NavLink></p>
        <p><NavLink to='/rates'>Курсы валют</NavLink></p>
        <p><NavLink to='/countries'>Страны</NavLink></p>
        <p onClick={exitHundler}>Выход</p>
    </nav>
  );
}

export default Header;
