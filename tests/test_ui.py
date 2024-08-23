# well at least I tried

# from typing import Any
# import tkinter.messagebox
# import tkinter.filedialog
# import tkinter.simpledialog
# from unittest.mock import patch, Mock
#
# from src.ui import provide_ui
#
#
# def test_provide_ui() -> None:
#     mock_file = Mock(return_value='test_ui_input.json')
#     mock_str = Mock(return_value='')
#     mock_bool = Mock(return_value=True)
#     mock_window = Mock(return_value=None)
#
#     tkinter.filedialog.askopenfilename = mock_file
#
#     tkinter.filedialog.askdirectory = mock_str
#     tkinter.simpledialog.askstring = mock_str
#
#     tkinter.messagebox.askyesno = mock_bool
#     tkinter.messagebox.askyesnocancel = mock_bool
#
#     tkinter.messagebox.showinfo = mock_window
#     tkinter.messagebox.showerror = mock_window
#
#     provide_ui()
#
#     assert True


# # @patch('tkinter.filedialog.askopenfilename')
# # @patch('tkinter.filedialog.askdirectory')
# # @patch('tkinter.simpledialog.askstring')
# # @patch('tkinter.messagebox')
# def test_provide_ui() -> None:
#     with patch('builtins.input', return_value=''):
#         with patch.object(tk.messagebox, 'showerror',
#                           return_value=None):
#             with patch.object(tk.messagebox, 'showinfo',
#                               return_value=None):
#                 with patch.object(tk.messagebox, 'askyesno',
#                                   return_value=True):
#                     with patch.object(tk.messagebox, 'askyesnocancel',
#                                       return_value=True):
#                         with patch.object(tk.simpledialog, 'askstring',
#                                           return_value=''):
#                             with patch.object(tk.filedialog, 'askdirectory',
#                                               return_value=''):
#                                 with patch.object(tk.filedialog, 'askopenfilename',
#                                                   return_value='test_ui_input.json'):
#                                     provide_ui()
#     assert True
