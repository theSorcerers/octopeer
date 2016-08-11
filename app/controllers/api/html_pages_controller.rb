class Api::HtmlPagesController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:html_page).permit(:dom, :session_id, :created_at)
  end
end
