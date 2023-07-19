import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import rootReducer from "./redux/reducers"; // Corrección en la importación del rootReducer
import { composeWithDevTools } from "redux-devtools-extension"; // Corrección en la importación de composeWithDevTools

const initialState = {};

const middleware = [thunk];

const store = createStore(
  rootReducer,
  initialState,
  // applyMiddleware(...middleware),
  composeWithDevTools(applyMiddleware(...middleware)) // Corrección aquí
);

export default store;

