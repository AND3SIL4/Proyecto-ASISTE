import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Error404 from "containers/errors/Error404";
import Home from "containers/pages/Home";
import { Provider } from "react-redux";
import store from "store";
import Prueba1 from "containers/pages/Prueba1";

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          {/* Error display */}
          <Route path="*" element={<Error404></Error404>}/>
        
          {/* Home display */}
          <Route path="/" element={<Home></Home>} />
          
          {/* Prueba1 display */}
          <Route path="/prueba1" element={<Prueba1></Prueba1>} />


        </Routes>
      </Router>
    </Provider>

  );
}

export default App;
