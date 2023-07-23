function AprendizInformacion({aprendices}) {
  return (
    <div>
      <div>
        Aprendices
        {
          aprendices && aprendices.map((aprendiz) => {
            <div>{aprendiz.nombres_aprendiz}</div>
          })
        }
      </div>
    </div>
  )
}

export default AprendizInformacion


