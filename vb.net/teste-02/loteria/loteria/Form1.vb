Public Class Form1


    Dim t1 As New List(Of Array) From {New Integer() {1, 3, 4, 8, 11, 12, 15, 16, 18, 19, 20, 22, 23, 24, 25}, New Integer() {1, 2, 3, 4, 7, 10, 11, 12, 13, 14, 16, 17, 20, 24, 25},
        New Integer() {1, 2, 3, 5, 9, 10, 11, 12, 13, 19, 21, 22, 23, 24, 25}, New Integer() {1, 2, 3, 5, 6, 13, 14, 16, 18, 19, 21, 22, 23, 24, 25}, New Integer() {1, 2, 4, 5, 8, 9, 10, 11, 14, 15, 16, 17, 18, 21, 25}, New Integer() {1, 3, 4, 7, 8, 9, 10, 11, 12, 13, 15, 18, 21, 22, 25}, New Integer() {2, 3, 4, 7, 8, 9, 14, 16, 17, 18, 19, 20, 22, 24, 25}, New Integer() {2, 5, 7, 8, 9, 10, 11, 12, 13, 16, 18, 19, 20, 21, 23}}
    Dim tentativas As Integer = 0
    Dim n_d_t As Integer = 0
    Dim isx As Integer = 0
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click

        Do While CheckedListBox1.Items.Count <> CheckedListBox1.CheckedItems.Count
            Dim numero_menor_que_dez As Integer = 0
            Dim r As New ArrayList
            Dim rnd As New Random
            Dim n1(t1.Count - 1) As Integer
            Me.Text = "Numero de tentativas = " & ProgressBar2.Value

            If tentativas >= 1000 Then

                isx += 1

                Dim objWriter As New System.IO.StreamWriter("C:\Temp\loteria\sorteio.txt", True)
                objWriter.WriteLine(TextBox1.Text)
                objWriter.Close()
                TextBox1.Text = ""
                tentativas = 0
            End If
            tentativas += 1
            n_d_t += 1
            'If rnd.Next(1,21) <= 12 Then
            Do While r.Count < 15
                Dim x As Integer = rnd.Next(1, 26)
                'Me.Text = x.ToString & " n n s " & (r.Count + 1).ToString
                ProgressBar1.Value = r.Count + 1
                If Not r.Contains(x) Then

                    'If x < 10 Then
                    'If numero_menor_que_dez <= 5 Then
                    'numero_menor_que_dez += 1
                    'r.Add(x)
                    'End If
                    'Else
                    'r.Add(x)
                    'End If

                    For ix As Integer = 1 To t1.Count
                        Dim num_d_num As Integer() = t1(ix - 1)
                        If num_d_num.Contains(x) Then
                            n1(ix - 1) += 1
                        End If
                    Next

                    r.Add(x)
                End If
                'Threading.Thread.Sleep(200)
            Loop

            r.Sort()
            Dim text_com_num As String = n_d_t.ToString & "/" & String.Join(",", r.ToArray)
            Dim media As New Double

            For Each n As Integer In n1
                text_com_num += "/" & n.ToString
                media += n
            Next

            media = (media / n1.Length)

            text_com_num += "/" & media.ToString("0.00") & vbNewLine

            If CheckedListBox1.Items.Contains(String.Join(",", r)) Then
                CheckedListBox1.SetItemChecked(CheckedListBox1.Items.IndexOf(String.Join(",", r)), True)
                TextBox2.AppendText(text_com_num & " numero de tentativas: " & n_d_t.ToString & " porcentagem de acerto: " & (tentativas / 100).ToString)
            End If

            TextBox1.AppendText(text_com_num)

            ProgressBar2.Value += 1


            If ProgressBar2.Value = ProgressBar2.Maximum Then
                ProgressBar2.Maximum = ProgressBar2.Maximum * 2
            End If


            Threading.Thread.Sleep(10)
            'End If 
        Loop
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim lista As New ArrayList
        For Each arr As Array In t1
            Dim num As Integer() = arr
            lista.Add(String.Join(",", num.ToArray))
        Next
        CheckedListBox1.DataSource = lista
    End Sub

End Class
