import axios from "axios";
import { GET_APRENDICES_FAIL, GET_APRENDICES_SUCCESS } from "./types";

export const get_aprendices = () => async (dispatch) => {
  const config = {
    headers: {
      Accept: "application/json",
    },
  };

  try {
    const res = await axios.get(
      `${process.env.REACT_APP_API_URL}/api/asistencia/aprendices`,
      config
    );

    if (res.status === 200) {
      dispatch({
        type: GET_APRENDICES_SUCCESS,
        payload: res.data,
      });
    } else {
      dispatch({
        type: GET_APRENDICES_FAIL,
      });
    }
  } catch (err) {
    dispatch({
      type: GET_APRENDICES_FAIL,
    });
  }
};
