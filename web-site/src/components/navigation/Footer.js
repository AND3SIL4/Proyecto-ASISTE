import { connect } from "react-redux";
import { NavLink } from "react-router-dom";
function Footer() {
  return (
    <nav>
      Footer
      <NavLink to={'/prueba1'}>Prueba1</NavLink>
      <NavLink to={'/prueba2'}>Prueba2</NavLink>
      <NavLink to={'/prueba3'}>Prueba3</NavLink>
    </nav>
  )
}

const mapStateToProp = state => ({
  
})

export default connect(mapStateToProp, {
  
}) (Footer)
