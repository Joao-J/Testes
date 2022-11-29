Imports System.Drawing

Public Class Form1

#Region "variaveis"
    Private start As Boolean = False

    Const tamanho As Integer = 30
#End Region

    Public Sub New()

        Me.InitializeComponent()
        Me.Width = 998
        Me.Height = 537

    End Sub


    Sub draw()
        Dim g As Graphics = pictureBox1.CreateGraphics
        Dim p As Pen
        p = New Pen(Color.Black, 1)

        For x As Integer = 0 To Me.Width / tamanho
            g.DrawLine(p, x * 30, 0, x * 30, Me.Height)
        Next
        For y As Integer = 0 To Me.Height / tamanho
            g.DrawLine(p, 0, y * tamanho, Me.Width, y * tamanho)
        Next
        p.Dispose()
    End Sub

    Sub Timer1Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If start = True Then
            draw()
        End If

    End Sub



    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Button1.Visible = False
        start = True

    End Sub
End Class

