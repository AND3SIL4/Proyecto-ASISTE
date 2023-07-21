import {
  GET_APRENDICES_FAIL,
  GET_APRENDICES_SUCCESS,
} from "../actions/aprendices/tipos";

const initialState = {
  aprendices: null,
};

export default function aprendices(state = initialState, action) {
  const { type, payload } = action;

  switch (type) {
    case GET_APRENDICES_SUCCESS:
      return {
        ...state,
        aprendices: payload.aprendices,
      };
    case GET_APRENDICES_FAIL:
      return {
        ...state,
        aprendices: null,
      };

    default:
      return state;
  }
}
