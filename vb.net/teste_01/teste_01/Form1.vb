Imports System.Drawing

Public Class Form1

#Region "variaveis"
    Private start As Boolean = False

    Const tamanho As Integer = 30
#End Region

    Public Sub New()

        Me.InitializeComponent()


    End Sub



    Sub draw()
        Dim g As Graphics = PictureBox1.CreateGraphics
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

    Private Sub PictureBox1_Click(sender As Object, e As EventArgs) Handles PictureBox1.Click
        Dim g As Graphics = PictureBox1.CreateGraphics
        Dim b As SolidBrush
        b = New SolidBrush(Color.Cyan)

        Dim x As Integer = (MousePosition.X - Me.Left) / tamanho
        If x > (MousePosition.X - Me.Left) / tamanho Then
            x -= 1
        End If

        Dim y As Integer = (MousePosition.Y - Me.Top) / tamanho
        If y > (MousePosition.Y - Me.Top - tamanho) / tamanho Then
            y -= 1
        End If
        g.FillRectangle(b, (x * tamanho), (y * tamanho), tamanho, tamanho)

    End Sub
End Class

