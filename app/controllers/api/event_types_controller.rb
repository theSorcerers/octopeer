class Api::EventTypesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:event_type).permit(:name)
  end
end
